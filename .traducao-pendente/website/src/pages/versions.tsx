/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

<<<<<<< pt
// ia-translated: true

import React from 'react';
import Layout from '@theme/Layout';
||||||| base_en
import React from 'react';
import Layout from '@theme/Layout';
=======
import type {PropSidebar} from '@docusaurus/plugin-content-docs';

import {DocsSidebarProvider} from '@docusaurus/plugin-content-docs/client';
>>>>>>> new_en
import useBaseUrl from '@docusaurus/useBaseUrl';
import DocRootLayout from '@theme/DocRoot/Layout';
import Layout from '@theme/Layout';

import versions from '../../versions.json';
// The versionsArchived mapping is a custom feature, NOT a Docusaurus feature
import versionsArchived from '../../versionsArchived.json';

const VersionItem = ({
  version,
  archivedDocumentationUrl,
  currentVersion,
}: {
  version: string;
  currentVersion: string;
  archivedDocumentationUrl?: string;
}) => {
  const versionName = version === 'next' ? 'main' : version;

  const isCurrentVersion = currentVersion === version;
  const isNext = version === 'next';
  const isRC = version.toUpperCase().indexOf('-RC') !== -1;

  const latestMajorVersion = versions[0].toUpperCase().replace('-RC', '');

  const documentationUrl = useBaseUrl(
    archivedDocumentationUrl ??
      `/docs/${isCurrentVersion ? '' : version + '/'}getting-started`
  );
  const documentationLink = <a href={documentationUrl}>Documentação</a>;

  let releaseNotesURL = 'https://github.com/react/react-native/releases';
  let releaseNotesTitle = 'Changelog';
  if (isNext) {
<<<<<<< pt
    releaseNotesURL = `https://github.com/facebook/react-native/compare/${latestMajorVersion}-stable...main`;
    releaseNotesTitle = 'Commits desde ' + latestMajorVersion;
||||||| base_en
    releaseNotesURL = `https://github.com/facebook/react-native/compare/${latestMajorVersion}-stable...main`;
    releaseNotesTitle = 'Commits since ' + latestMajorVersion;
=======
    releaseNotesURL = `https://github.com/react/react-native/compare/${latestMajorVersion}-stable...main`;
    releaseNotesTitle = 'Commits since ' + latestMajorVersion;
>>>>>>> new_en
  } else if (!isRC) {
    releaseNotesURL = `https://github.com/react/react-native/releases/tag/v${version}.0`;
  }

  const releaseNotesLink = <a href={releaseNotesURL}>{releaseNotesTitle}</a>;

  return (
    <tr>
      <th>{versionName}</th>
      <td>{documentationLink}</td>
      <td>{releaseNotesLink}</td>
    </tr>
  );
};

// Mirrors the `releases` sidebar in sidebarsReleases.ts so the /versions page
// (a standalone React page, not a doc) renders the same sidebar. Keep in sync.
const releasesSidebar: PropSidebar = [
  {type: 'link', href: '/releases/overview', label: 'Overview'},
  {type: 'link', href: '/releases/branches', label: 'Branches'},
  {
    type: 'link',
    href: '/releases/versioning-policy',
    label: 'Versioning Policy',
  },
  {type: 'link', href: '/versions', label: 'Docs Versions'},
];

const Versions = () => {
  const currentVersion = versions.length > 0 ? versions[0] : null;
  const latestVersions = ['next'].concat(
    versions.filter(version => version.indexOf('-RC') !== -1)
  );
  const stableVersions = versions.filter(
    version => version.indexOf('-RC') === -1 && version !== currentVersion
  );

  return (
<<<<<<< pt
    <Layout title="Versões" wrapperClassName="versions-page">
      <h1>Versões do React Native</h1>
      <p>
        As versões de código aberto do React Native seguem um processo de release coordenado
        no GitHub através do repositório{' '}
        <a
          href={'https://github.com/reactwg/react-native-releases/discussions'}>
          <code>react-native-releases</code>
        </a>{' '}
        . Novas versões são criadas a partir da branch <code>main</code> de{' '}
        <a href={'https://github.com/facebook/react-native'}>
          <code>facebook/react-native</code>
        </a>
        . Elas seguirão um processo de Release Candidate para permitir que contribuidores
        como você{' '}
        <a href={useBaseUrl('docs/upgrading')}>verifiquem as mudanças</a> e
        identifiquem quaisquer problemas{' '}
        <a href="https://github.com/facebook/react-native/issues">
          escrevendo relatórios de bugs claros e acionáveis
        </a>
        . Eventualmente, o release candidate será promovido a estável.
      </p>
      <h2>Próxima versão (Não lançada)</h2>
      <p>
        Para ver quais mudanças estão chegando e fornecer melhor feedback aos
        contribuidores do React Native, use o último release candidate quando possível.
        As mudanças introduzidas em um release candidate terão sido enviadas para
        apps da Facebook em produção por mais de duas semanas no momento em que o release
        candidate é criado.
      </p>
      <table className="versions">
        <tbody>
          {latestVersions.map(version => (
            <VersionItem
              key={'version_' + version}
              version={version}
              currentVersion={currentVersion}
            />
          ))}
        </tbody>
      </table>
      <h2>Última versão</h2>
      <p>
        A versão estável mais recente será usada automaticamente sempre que um novo
        projeto for criado usando o comando <code>npx react-native init</code>.
      </p>
      <table className="versions">
        <tbody>
          <VersionItem
            key={'version_' + currentVersion}
            version={currentVersion}
            currentVersion={currentVersion}
          />
        </tbody>
      </table>
      <h2>Versões anteriores</h2>
      <table className="versions">
        <tbody>
          {stableVersions.map(version => (
            <VersionItem
              key={'version_' + version}
              version={version}
              currentVersion={currentVersion}
            />
          ))}
        </tbody>
      </table>
      <h2>Versões arquivadas</h2>
      <p>
        A documentação para versões não mantidas pode ser encontrada em snapshots de arquivo do website,
        hospedados como sites separados.
      </p>
      <table className="versions">
        <tbody>
          {Object.entries(versionsArchived).map(
            ([version, archivedDocumentationUrl]) => (
              <VersionItem
                key={'version_' + version}
                version={version}
                archivedDocumentationUrl={archivedDocumentationUrl}
                currentVersion={currentVersion}
              />
            )
          )}
        </tbody>
      </table>
      <p>
        A documentação para versões abaixo de <code>0.60</code> pode ser encontrada no
        site separado chamado{' '}
        <a href="https://archive.reactnative.dev/versions">
          React Native Archive
        </a>
        .
      </p>
||||||| base_en
    <Layout title="Versions" wrapperClassName="versions-page">
      <h1>React Native versions</h1>
      <p>
        Open source React Native releases follow a release train that is
        coordinated on GitHub through the{' '}
        <a
          href={'https://github.com/reactwg/react-native-releases/discussions'}>
          <code>react-native-releases</code>
        </a>{' '}
        repository. New releases are created off the <code>main</code> branch of{' '}
        <a href={'https://github.com/facebook/react-native'}>
          <code>facebook/react-native</code>
        </a>
        . They will follow a Release Candidate process to allow contributors
        like yourself to{' '}
        <a href={useBaseUrl('docs/upgrading')}>verify the changes</a> and to
        identify any issues by{' '}
        <a href="https://github.com/facebook/react-native/issues">
          writing clear, actionable bug reports
        </a>
        . Eventually, the release candidate will be promoted to stable.
      </p>
      <h2>Next version (Unreleased)</h2>
      <p>
        To see what changes are coming and provide better feedback to React
        Native contributors, use the latest release candidate when possible.
        Changes introduced in a release candidate will have been shipped to
        production Facebook apps for over two weeks by the time the release
        candidate is cut.
      </p>
      <table className="versions">
        <tbody>
          {latestVersions.map(version => (
            <VersionItem
              key={'version_' + version}
              version={version}
              currentVersion={currentVersion}
            />
          ))}
        </tbody>
      </table>
      <h2>Latest version</h2>
      <p>
        The most recent stable version will be used automatically whenever a new
        project is created using the <code>npx react-native init</code> command.
      </p>
      <table className="versions">
        <tbody>
          <VersionItem
            key={'version_' + currentVersion}
            version={currentVersion}
            currentVersion={currentVersion}
          />
        </tbody>
      </table>
      <h2>Previous versions</h2>
      <table className="versions">
        <tbody>
          {stableVersions.map(version => (
            <VersionItem
              key={'version_' + version}
              version={version}
              currentVersion={currentVersion}
            />
          ))}
        </tbody>
      </table>
      <h2>Archived versions</h2>
      <p>
        The documentation for unmaintained versions can be found on website
        archive snapshots, hosted as separate sites.
      </p>
      <table className="versions">
        <tbody>
          {Object.entries(versionsArchived).map(
            ([version, archivedDocumentationUrl]) => (
              <VersionItem
                key={'version_' + version}
                version={version}
                archivedDocumentationUrl={archivedDocumentationUrl}
                currentVersion={currentVersion}
              />
            )
          )}
        </tbody>
      </table>
      <p>
        The documentation for versions below <code>0.60</code> can be found on
        the separate website called{' '}
        <a href="https://archive.reactnative.dev/versions">
          React Native Archive
        </a>
        .
      </p>
=======
    <Layout title="Versions">
      <DocsSidebarProvider name="releases" items={releasesSidebar}>
        <DocRootLayout>
          <div className="versions-page">
            <h1>Docs Versions</h1>
            <h2>Next version (Unreleased)</h2>
            <p>
              Ahead of each stable release, React Native publishes a series of
              release candidates. Learn more about the{' '}
              <a href="/releases/overview#release-channels">release channels</a>
              .
            </p>
            <div className="table-wrapper">
              <table className="versions">
                <tbody>
                  {latestVersions.map(version => (
                    <VersionItem
                      key={'version_' + version}
                      version={version}
                      currentVersion={currentVersion}
                    />
                  ))}
                </tbody>
              </table>
            </div>
            <h2>Latest version</h2>
            <div className="table-wrapper">
              <table className="versions">
                <tbody>
                  <VersionItem
                    key={'version_' + currentVersion}
                    version={currentVersion}
                    currentVersion={currentVersion}
                  />
                </tbody>
              </table>
            </div>
            <h2>Previous versions</h2>
            <div className="table-wrapper">
              <table className="versions">
                <tbody>
                  {stableVersions.map(version => (
                    <VersionItem
                      key={'version_' + version}
                      version={version}
                      currentVersion={currentVersion}
                    />
                  ))}
                </tbody>
              </table>
            </div>
            <h3>Archived versions</h3>
            <p>
              The documentation for unmaintained versions can be found on
              website archive snapshots, hosted as separate sites.
            </p>
            <div className="table-wrapper">
              <table className="versions">
                <tbody>
                  {Object.entries(versionsArchived).map(
                    ([version, archivedDocumentationUrl]) => (
                      <VersionItem
                        key={'version_' + version}
                        version={version}
                        archivedDocumentationUrl={archivedDocumentationUrl}
                        currentVersion={currentVersion}
                      />
                    )
                  )}
                </tbody>
              </table>
            </div>
            <p>
              The documentation for versions below <code>0.60</code> can be
              found on the separate website called{' '}
              <a href="https://archive.reactnative.dev/versions">
                React Native Archive
              </a>
              .
            </p>
          </div>
        </DocRootLayout>
      </DocsSidebarProvider>
>>>>>>> new_en
    </Layout>
  );
};

export default Versions;
