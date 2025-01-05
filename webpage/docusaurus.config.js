// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Vehicle Network Standards',
  tagline: 'Detailed  resources on automotive networking and systems',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
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
                to: '/docs/GLOSSARY/info',
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
    }),
};

export default config;
