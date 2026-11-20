/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// ia-translated: true

import React from 'react';
import GitHubButton from 'react-github-btn';
import {useColorMode} from '@docusaurus/theme-common';

import Logo from '../Logo';
import GridBackground from './GridBackground';
import FloorBackground from './FloorBackground';
import Devices from './Devices';

import styles from './styles.module.css';

function Hero() {
  const {colorMode} = useColorMode();
  return (
    <div className={styles.container}>
      <div className={styles.socialLinks}>
        <a
          className="twitter-follow-button"
          href="https://x.com/reactnative"
          data-show-count="false"
          data-size="large">
          Siga @reactnative
        </a>
        <GitHubButton
          href="https://github.com/react/react-native"
          data-icon="octicon-star"
          data-size="large"
          data-color-scheme={colorMode}
<<<<<<< pt
          aria-label="Marque facebook/react-native como favorito no GitHub">
          Favoritar
||||||| base_en
          aria-label="Star facebook/react-native on GitHub">
          Star
=======
          aria-label="Star react/react-native on GitHub">
          Star
>>>>>>> new_en
        </GitHubButton>
      </div>
      <div className={styles.backgroundContainer}>
        <div className={styles.gridBackground}>
          <GridBackground />
        </div>
        <div className={styles.devices}>
          <Devices />
        </div>
        <div className={styles.floorBackground}>
          <FloorBackground />
        </div>
      </div>
      <div className={styles.content}>
        <Logo />
        <h1 className={styles.title}>React Native</h1>
        <h2 className={styles.subtitle}>Aprenda uma vez, escreva em qualquer lugar.</h2>
        <div className={styles.buttonContainer}>
          <a href="/docs/environment-setup" className={styles.primaryButton}>
            Começar
          </a>
          <a href="/docs/getting-started" className={styles.secondaryButton}>
            Aprenda o Básico
          </a>
        </div>
      </div>
    </div>
  );
}

export default Hero;
