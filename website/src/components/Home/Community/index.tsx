/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// ia-translated: true

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
      <SectionTitle
        title="Apoiado pela Meta. Impulsionado pela comunidade."
        description={
          <>
            O React Native é usado em milhares de apps, e é provável que
            <br />
            você já tenha usado um deles.
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
                    <img src={imgSource} alt={app.name} />
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
        Veja todos os apps em destaque
      </a>
      <div className={styles.communityNote}>
        <p>
          A Meta lançou o React Native em 2015 e o mantém desde então.
          <br />
          Hoje, o React Native é apoiado por contribuições de indivíduos e
          empresas do mundo todo, incluindo:
        </p>
        <PartnersShowcase />
        <p>
          Além disso, nossa comunidade está sempre lançando projetos novos e
          empolgantes e indo além de Android e iOS com iniciativas como{' '}
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
          e{' '}
          <a
            href="https://necolas.github.io/react-native-web/"
            target="_blank"
            rel="noopener noreferrer">
            React Native Web
          </a>
        </p>
      </div>
      <a
        href="https://github.com/react/react-native/blob/main/ECOSYSTEM.md"
        target="_blank"
        rel="noopener noreferrer"
        className={styles.secondaryButton}>
        Saiba mais sobre o ecossistema
      </a>
    </Section>
  );
}

export default Community;
