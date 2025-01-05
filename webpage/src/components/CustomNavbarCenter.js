// src/components/CustomNavbarCenter.js

import React from 'react';
import { useThemeConfig } from '@docusaurus/theme-common';
import Link from '@docusaurus/Link';
import styles from './CustomNavbarCenter.module.css';

export default function CustomNavbarCenter() {
  const { navbar } = useThemeConfig();

  return (
    <div className={styles.centerItems}>
      {/* Add your centered items here */}
      <Link to="/blog" className={styles.navLink}>
        Blog
      </Link>
      {/* Add more centered links as needed */}
    </div>
  );
}
