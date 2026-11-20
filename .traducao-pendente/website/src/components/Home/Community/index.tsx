/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

<<<<<<< pt
// ia-translated: true

import React from 'react';

||||||| base_en
import React from 'react';

=======
>>>>>>> new_en
import useBaseUrl from '@docusaurus/useBaseUrl';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import {ShowcaseData} from '@site/src/types';

import PartnersShowcase from './PartnersShowcase';
import Section from '../Section';
import SectionTitle from '../SectionTitle';

import styles from './styles.module.css';

function Community() {
  const {siteConfig} = useDocusaurusContext();
  const apps = Object.values(siteConfig.customFields?.users as ShowcaseData)
    .flat()
    .filter(app => Boolean(app.pinned));

  return (
    <Section>
<<<<<<< pt
      <SectionTitle title="Apoiado pela Meta. Impulsionado pela comunidade." />
      <div className={styles.featureContainer}>
        <div>
          <p>
            A Meta lançou o React Native em 2015 e tem mantido desde então.
          </p>
          <p>
            Em 2018, React Native teve o{' '}
            <a href="https://octoverse.github.com/2018/projects#repositories">
              2º maior
            </a>{' '}
            número de contribuidores para qualquer repositório no GitHub. Hoje, React
            Native é apoiado por contribuições de indivíduos e empresas
            ao redor do mundo incluindo{' '}
            <span>
              <a href="https://callstack.com/">Callstack</a>
            </span>
            ,{' '}
            <span>
              <a href="https://expo.io/">Expo</a>
            </span>
            , <a href="https://infinite.red/">Infinite Red</a>,{' '}
            <a href="https://www.microsoft.com/">Microsoft</a> e{' '}
            <a href="https://swmansion.com/">Software Mansion</a>.
          </p>
          <p>
            Nossa comunidade está sempre lançando novos projetos empolgantes e explorando
            plataformas além de Android e iOS com repositórios como{' '}
            <span>
              <a href="https://github.com/microsoft/react-native-windows#readme">
                React Native Windows
              </a>
            </span>
            ,{' '}
            <a href="https://github.com/microsoft/react-native-macos#readme">
              React Native macOS
            </a>{' '}
            e{' '}
            <a href="https://github.com/necolas/react-native-web#readme">
              React Native Web
            </a>
            .
          </p>
        </div>
        <div>
          <p>
            React Native está sendo usado em milhares de aplicativos, mas é provável
            que você já tenha usado em um desses aplicativos:
          </p>
          <ul className="AppList">
            {apps.map((app, i) => {
              const imgSource = !app.icon.startsWith('http')
                ? useBaseUrl('img/showcase/' + app.icon)
                : app.icon;
              return (
                <li key={i} className="item">
                  {app.infoLink ? (
                    <a href={app.infoLink}>
                      <img src={imgSource} alt={app.name} />
                    </a>
                  ) : (
||||||| base_en
      <SectionTitle title="Meta supported. Community driven." />
      <div className={styles.featureContainer}>
        <div>
          <p>
            Meta released React Native in 2015 and has been maintaining it ever
            since.
          </p>
          <p>
            In 2018, React Native had the{' '}
            <a href="https://octoverse.github.com/2018/projects#repositories">
              2nd highest
            </a>{' '}
            number of contributors for any repository in GitHub. Today, React
            Native is supported by contributions from individuals and companies
            around the world including{' '}
            <span>
              <a href="https://callstack.com/">Callstack</a>
            </span>
            ,{' '}
            <span>
              <a href="https://expo.io/">Expo</a>
            </span>
            , <a href="https://infinite.red/">Infinite Red</a>,{' '}
            <a href="https://www.microsoft.com/">Microsoft</a> and{' '}
            <a href="https://swmansion.com/">Software Mansion</a>.
          </p>
          <p>
            Our community is always shipping exciting new projects and exploring
            platforms beyond Android and iOS with repos like{' '}
            <span>
              <a href="https://github.com/microsoft/react-native-windows#readme">
                React Native Windows
              </a>
            </span>
            ,{' '}
            <a href="https://github.com/microsoft/react-native-macos#readme">
              React Native macOS
            </a>{' '}
            and{' '}
            <a href="https://github.com/necolas/react-native-web#readme">
              React Native Web
            </a>
            .
          </p>
        </div>
        <div>
          <p>
            React Native is being used in thousands of apps, but it's likely
            you've already used it in one of these apps:
          </p>
          <ul className="AppList">
            {apps.map((app, i) => {
              const imgSource = !app.icon.startsWith('http')
                ? useBaseUrl('img/showcase/' + app.icon)
                : app.icon;
              return (
                <li key={i} className="item">
                  {app.infoLink ? (
                    <a href={app.infoLink}>
                      <img src={imgSource} alt={app.name} />
                    </a>
                  ) : (
=======
      <SectionTitle
        title="Meta supported. Community driven."
        description={
          <>
            React Native is being used in thousands of apps, but it's likely
            <br />
            you've already used it in one of these apps.
          </>
        }
      />
      <div className={styles.featureContainer}>
        <ul className={styles.appList}>
          {apps.map((app, i) => {
            const imgSource = !app.icon.startsWith('http')
              ? useBaseUrl('img/showcase/' + app.icon)
              : app.icon;
            return (
              <li key={i} className="item">
                {app.infoLink ? (
                  <a
                    href={app.infoLink}
                    target="_blank"
                    rel="noopener noreferrer">
>>>>>>> new_en
                    <img src={imgSource} alt={app.name} />
<<<<<<< pt
                  )}
                </li>
              );
            })}
          </ul>
          <p>
            e <a href={useBaseUrl(`showcase`)}>muito mais</a>.
          </p>
        </div>
||||||| base_en
                  )}
                </li>
              );
            })}
          </ul>
          <p>
            and <a href={useBaseUrl(`showcase`)}>many more</a>.
          </p>
        </div>
=======
                  </a>
                ) : (
                  <img src={imgSource} alt={app.name} />
                )}
              </li>
            );
          })}
        </ul>
      </div>
      <a href={useBaseUrl(`showcase`)} className={styles.secondaryButton}>
        See all featured apps
      </a>
      <div className={styles.communityNote}>
        <p>
          Meta released React Native in 2015 and has been maintaining it ever
          since.
          <br />
          Today, React Native is supported by contributions from individuals and
          companies around the world including:
        </p>
        <PartnersShowcase />
        <p>
          Additionally, our community is always shipping exciting new projects
          and expanding beyond Android and iOS with initiatives like{' '}
          <a
            href="https://microsoft.github.io/react-native-windows/"
            target="_blank"
            rel="noopener noreferrer">
            React Native Windows
          </a>
          ,{' '}
          <a
            href="https://microsoft.github.io/react-native-macos/"
            target="_blank"
            rel="noopener noreferrer">
            React Native macOS
          </a>{' '}
          and{' '}
          <a
            href="https://necolas.github.io/react-native-web/"
            target="_blank"
            rel="noopener noreferrer">
            React Native Web
          </a>
        </p>
>>>>>>> new_en
      </div>
      <a
        href="https://github.com/react/react-native/blob/main/ECOSYSTEM.md"
        target="_blank"
        rel="noopener noreferrer"
        className={styles.secondaryButton}>
        Learn more about the Ecosystem
      </a>
    </Section>
  );
}

export default Community;
