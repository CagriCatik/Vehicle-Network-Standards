import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'CAN (Controller Area Network)',
    // Svg: require('@site/static/img/undraw_data_processing.svg').default,
    description: (
      <>
        Learn about the widely-used Controller Area Network (CAN) protocol, its architecture, and practical use cases in modern automotive systems.
      </>
    ),
  },
  {
    title: 'LIN (Local Interconnect Network)',
    // Svg: require('@site/static/img/undraw_networking.svg').default,
    description: (
      <>
        Explore the simplicity and efficiency of the LIN protocol, ideal for low-cost, low-speed vehicle networks.
      </>
    ),
  },
  {
    title: 'FlexRay',
    // Svg: require('@site/static/img/undraw_connected_world.svg').default,
    description: (
      <>
        Delve into the high-speed, deterministic communication offered by FlexRay, designed for safety-critical automotive applications.
      </>
    ),
  },
  {
    title: 'SOME/IP (Scalable service-Oriented Middleware over IP)',
    // Svg: require('@site/static/img/undraw_server_cluster.svg').default,
    description: (
      <>
        Understand how SOME/IP enables efficient communication in service-oriented architectures within automotive Ethernet networks.
      </>
    ),
  },
  {
    title: 'DoIP (Diagnostics over IP)',
    // Svg: require('@site/static/img/undraw_debugging.svg').default,
    description: (
      <>
        Learn about the Diagnostics over IP protocol, essential for vehicle diagnostics in modern Ethernet-based systems.
      </>
    ),
  },
  {
    title: 'XCP (Universal Measurement and Calibration Protocol)',
    // Svg: require('@site/static/img/undraw_calibration.svg').default,
    description: (
      <>
        Gain insights into XCP, the protocol for real-time measurement and calibration of ECU parameters during development.
      </>
    ),
  },
  {
    title: 'Automotive Ethernet',
    // Svg: require('@site/static/img/undraw_fast_car.svg').default,
    description: (
      <>
        Discover the importance of Ethernet in automotive networks, supporting high-bandwidth communication for ADAS and infotainment.
      </>
    ),
  },

  {
    title: 'UDS (Unified Diagnostic Services)',
    // Svg: require('@site/static/img/undraw_secure_server.svg').default,
    description: (
      <>
        Understand UDS, the ISO-standardized diagnostic communication protocol used for vehicle diagnostics and reprogramming in ECUs.
      </>
    ),
  },

  {
    title: 'AUTOSAR (Automotive Open System Architecture)',
    // Svg: require('@site/static/img/undraw_coding.svg').default,
    description: (
      <>
        Explore AUTOSAR, the standardized automotive software architecture designed to improve interoperability, scalability, and software reuse.
      </>
    ),
  },
];

function Feature({title, description}) {
  return (
    <div className={clsx('col col--4')}>
      {/* Uncomment the following block if SVGs are available */}
      {/* 
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      */}
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}


export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
