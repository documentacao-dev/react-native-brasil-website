/**
 * Plugin remark do React Native Brasil: põe um aviso no topo de toda página de
 * documentação que ainda não foi traduzida.
 *
 * Uma página conta como traduzida quando tem `ia-translated: true` no
 * frontmatter ou `<!-- ia-translated: true -->` (ou `{/* ia-translated: true *\/}`)
 * na primeira linha, a mesma regra de tool/traducao/escopo.py. A decisão é
 * tomada no build, lendo o arquivo-fonte. Parciais (`_*.md`, `_*.mdx`) não
 * recebem aviso: são importados dentro de outras páginas.
 *
 * Registrado só nos plugins de docs (commonDocsOptions.remarkPlugins), então
 * não aparece no blog nem nas páginas soltas (home, vitrine...).
 */
import fs from 'fs';
import path from 'path';
import type {Root, RootContent} from 'mdast';

const REPO_BLOB =
  'https://github.com/documentacao-dev/react-native-brasil-website/blob/main/';
const RAIZ_REPO = path.resolve(__dirname, '..', '..');

const FRONTMATTER = /^---\r?\n([\s\S]*?)\r?\n---[ \t]*(?:\r?\n|$)/;
const FLAG_FM = /^ia-translated:\s*true\s*$/m;
const FLAG_COMENTARIO =
  /^\s*(<!--\s*ia-translated:\s*true\s*-->|\{\/\*\s*ia-translated:\s*true\s*\*\/\})/;

export function traduzida(fonte: string): boolean {
  const fm = FRONTMATTER.exec(fonte);
  if (fm) {
    return FLAG_FM.test(fm[1]);
  }
  return FLAG_COMENTARIO.test(fonte);
}

function aviso(url: string): RootContent {
  // Nó JSX (MDX) equivalente a:
  // <div className="alert alert--warning aviso-nao-traduzido" role="note">
  //   <p>Esta página ainda está em inglês. ... <a href={url}>Traduza no GitHub →</a></p>
  // </div>
  return {
    type: 'mdxJsxFlowElement',
    name: 'div',
    attributes: [
      {
        type: 'mdxJsxAttribute',
        name: 'className',
        value: 'alert alert--warning aviso-nao-traduzido',
      },
      {type: 'mdxJsxAttribute', name: 'role', value: 'note'},
      {
        type: 'mdxJsxAttribute',
        name: 'aria-label',
        value: 'Página não traduzida',
      },
    ],
    children: [
      {
        type: 'paragraph',
        children: [
          {
            type: 'text',
            value:
              'Esta página ainda está em inglês. A tradução para o português ainda não chegou aqui. Quer ajudar? ',
          },
          {
            type: 'link',
            url,
            children: [{type: 'text', value: 'Traduza no GitHub →'}],
          },
        ],
      },
    ],
  } as unknown as RootContent;
}

export default function avisoNaoTraduzido() {
  return (root: Root, file: {path?: string; value?: unknown}) => {
    const caminho = file.path;
    if (!caminho || !/\.mdx?$/.test(caminho)) {
      return;
    }
    if (path.basename(caminho).startsWith('_')) {
      return;
    }
    let fonte: string;
    try {
      fonte = fs.readFileSync(caminho, 'utf8');
    } catch {
      return;
    }
    if (traduzida(fonte)) {
      return;
    }
    const relativo = path
      .relative(RAIZ_REPO, caminho)
      .split(path.sep)
      .join('/');
    if (relativo.startsWith('..')) {
      return;
    }
    // Depois dos imports e de um `# Título` inicial, se houver; senão no topo
    // do conteúdo (o título do frontmatter é desenhado pelo tema antes dele).
    // Se o primeiro título não for o primeiro nó, o aviso fica antes dele.
    let i = 0;
    while (i < root.children.length && root.children[i].type === 'mdxjsEsm') {
      i++;
    }
    // O plugin contentTitle do Docusaurus (que roda antes) embrulha o `# Título`
    // inicial num <header>; o aviso vai logo depois dele.
    const primeiro = root.children[i] as unknown as {
      type: string;
      name?: string;
      depth?: number;
    };
    if (
      primeiro &&
      ((primeiro.type === 'heading' && primeiro.depth === 1) ||
        (primeiro.type === 'mdxJsxFlowElement' && primeiro.name === 'header'))
    ) {
      i++;
    }
    root.children.splice(i, 0, aviso(REPO_BLOB + relativo));
  };
}
