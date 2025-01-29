// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import { themes as prismThemes } from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

 /** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Vehicle Network Standards',
  tagline: 'Detailed resources on automotive networking and systems',
  favicon: 'img/favicon.ico',
  url: 'https://CagriCatik.github.io',
  baseUrl: '/Vehicle-Network-Standards/',
  organizationName: 'CagriCatik', 
  projectName: 'Vehicle-Network-Standards',
  deploymentBranch: 'gh-pages',
  onBrokenLinks: 'ignore',
  onBrokenMarkdownLinks: 'ignore',
  themes: ['@docusaurus/theme-mermaid'],
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /**
       * @type {import('@docusaurus/preset-classic').Options}
       */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({    
      navbar: {
        title: 'VNS',
        logo: {
          alt: 'My Site Logo',
          src: 'img/car.svg',
        },
        items: [

          {
            type: 'docSidebar',
            sidebarId: 'autosarSidebar',
            position: 'right',
            label: 'AUTOSAR',
          },

          {
            type: 'docSidebar',
            sidebarId: 'sovaSidebar',
            position: 'right',
            label: 'SOVA',
          },
          {
            type: 'docSidebar',
            sidebarId: 'sovdSidebar',
            position: 'right',
            label: 'SOVD',
          },
          {
            type: 'docSidebar',
            sidebarId: 'udsSidebar',
            position: 'right',
            label: 'UDS',
          },
          {
            type: 'docSidebar',
            sidebarId: 'canSidebar',
            position: 'right',
            label: 'CAN',
          },
          {
            type: 'docSidebar',
            sidebarId: 'linSidebar',
            position: 'right',
            label: 'LIN',
          },
          {
            type: 'docSidebar',
            sidebarId: 'flexraySidebar',
            position: 'right',
            label: 'FlexRay',
          },
          {
            type: 'docSidebar',
            sidebarId: 'ethernetSidebar',
            position: 'right',
            label: 'Ethernet',
          },
          {
            type: 'docSidebar',
            sidebarId: 'doipSidebar',
            position: 'right',
            label: 'DoIP',
          },
          {
            type: 'docSidebar',
            sidebarId: 'someipSidebar',
            position: 'right',
            label: 'SOME/IP',
          },
          {
            type: 'docSidebar',
            sidebarId: 'xcpSidebar',
            position: 'right',
            label: 'XCP',
          },
          {
            type: 'docSidebar',
            sidebarId: 'secocSidebar',
            position: 'right',
            label: 'SecOC',
          },
          {
            type: 'docSidebar',
            sidebarId: 'iso26262Sidebar',
            position: 'right',
            label: 'ISO26262',
          },
          {
            type: 'docSidebar',
            sidebarId: 'fmeaSidebar',
            position: 'right',
            label: 'FMEA',
          },

          {
            type: 'docSidebar',
            sidebarId: 'otaSidebar',
            position: 'right',
            label: 'OTA',
          },
          {
            to: '/blog', 
            label: 'Blog', 
            position: 'right'
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Protocols',
            items: [
              {
                label: 'CAN',
                to: '/docs/intro',
              },
              {
                label: 'LIN',
                to: '/docs/intro',
              },
              {
                label: 'FlexRay',
                to: '/docs/intro',
              },
              {
                label: 'Ethernet',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'Diagnostic',
            items: [
              {
                label: 'UDS',
                to: '/docs/UDS/Getting-Started',
              },
              {
                label: 'DoIP',
                to: '/docs/UDS/Getting-Started',
              },
              {
                label: 'SOVD',
                to: '/docs/UDS/Getting-Started',
              },
            ],
          },
          {
            title: 'Architecture',
            items: [
              {
                label: 'AUTOSAR',
                to: '/docs/AUTOSAR/Getting-Started',
              },
              {
                label: 'SOVA',
                to: '/docs/SOVA/Getting-Started',
              },
              {
                label: 'SOME/IP',
                to: '/docs/SOME-IP/Getting-Started',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Blog',
                to: '/blog',
              },
              {
                label: 'Sources',
                to: '/docs/SOURCES/info',
              },
              {
                label: 'Glossary',
                to: '/docs/Glossary/Getting-Started',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/CagriCatik/Vehicle-Network-Standards',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Vehicle Network Standards.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
      mermaid: {
        theme: { light: 'neutral', dark: 'forest' }, // Add this section
      },
    }),
};

export default config;
