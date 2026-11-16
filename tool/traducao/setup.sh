#!/usr/bin/env bash
# Prepara um ambiente do zero (sessão nova na nuvem, runner do Actions) para
# os scripts de tool/traducao/: confere o Python 3 e o PyYAML, configura o
# remote `upstream` (facebook/react-native-website) e busca histórico
# suficiente para achar o último commit sincronizado.
#
#   bash tool/traducao/setup.sh
#
# O build do site (Node 22 + Yarn, `yarn install && yarn build` em website/)
# não é necessário para os scripts; o job `build` do pre-merge.yml faz isso
# em todo PR.
set -euo pipefail
cd "$(dirname "$0")/../.."

command -v python3 >/dev/null || { echo "Falta o python3"; exit 1; }
if ! python3 -c 'import yaml' 2>/dev/null; then
  python3 -m pip install --quiet --user pyyaml 2>/dev/null \
    || python3 -m pip install --quiet --user --break-system-packages pyyaml
fi

if ! git remote get-url upstream >/dev/null 2>&1; then
  git remote add upstream https://github.com/facebook/react-native-website.git
fi
git fetch -q --depth=3000 upstream main
if git rev-parse --is-shallow-repository | grep -q true; then
  git fetch -q --depth=3000 origin "$(git rev-parse --abbrev-ref HEAD)" || true
fi

base=$(cat tool/traducao/ultimo-sync-upstream.txt)
if git cat-file -e "$base" 2>/dev/null; then
  echo "Pronto. Upstream: $(git rev-list --count "$base"..upstream/main) commit(s) desde ${base:0:9}."
else
  echo "Aviso: o commit do último sync (${base:0:9}) não está no histórico buscado."
fi
