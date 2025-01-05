import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'AUTOSAR (Automotive Open System Architecture)',
    description: (
      <>
        Explore AUTOSAR, the standardized automotive software architecture designed to improve interoperability, scalability, and software reuse across the automotive industry.
      </>
    ),
  },
  {
    title: 'CAN (Controller Area Network)',
    description: (
      <>
        Learn about the widely-used <a href="/docs/CAN/Getting-Started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>CAN</a> protocol, including its architecture and practical use cases in modern automotive systems. 
        .
      </>
    ),
  },
  
  
  {
    title: 'DoIP (Diagnostics over IP)',
    description: (
      <>
        Learn about the <a href="/docs/DoIP/Getting-Started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>DoIP</a>, essential for vehicle diagnostics in modern Ethernet-based systems.
      </>
    ),
  },
  {
    title: 'Ethernet',
    description: (
      <>
        Discover the importance of <a href="/docs/Ethernet/Getting-Started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>Ethernet</a> in automotive networks, supporting high-bandwidth communication for ADAS and infotainment.
      </>
    ),
  },
  {
    title: 'FlexRay',
    description: (
      <>
        Delve into the high-speed, deterministic communication offered by <a href="/docs/FLEXRAY/Getting-Started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>FlexRay</a>, designed for safety-critical automotive applications.
      </>
    ),
  },
  {
    title: 'LIN (Local Interconnect Network)',
    description: (
      <>
        Explore the simplicity and efficiency of the <a href="/docs/LIN/Getting-Started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>LIN</a> protocol, ideal for low-cost, low-speed vehicle networks.
      </>
    ),
  },
  {
    title: 'SecOC (Secure Onboard Communication)',
    description: (
      <>
        Understand SecOC, the automotive cybersecurity standard ensuring secure and reliable communication within vehicle networks.
      </>
    ),
  },
  {
    title: 'SOME/IP (Scalable service-Oriented Middleware over IP)',
    description: (
      <>
        Learn how <a href="/docs/SOME-IP/Getting-Started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>SOME/IP</a> enables efficient communication in service-oriented architectures within automotive Ethernet networks.
      </>
    ),
  },
  {
    title: 'SOVA (Service-Oriented Vehicle Architecture)',
    description: (
      <>
        Explore SOVA, the architecture that facilitates modular development and integration of vehicle services and applications.
      </>
    ),
  },
  {
    title: 'SOVD (Service-Oriented Vehicle Diagnostics)',
    description: (
      <>
        Gain insights into SOVD, a modern approach to vehicle diagnostics leveraging service-oriented architectures for scalability and efficiency.
      </>
    ),
  },
  {
    title: 'UDS (Unified Diagnostic Services)',
    description: (
      <>
        Understand UDS, the ISO-standardized diagnostic communication protocol used for vehicle diagnostics and ECU reprogramming in automotive systems.
      </>
    ),
  },
  {
    title: 'XCP (Universal Measurement and Calibration Protocol)',
    description: (
      <>
        Learn about <a href="/docs/XCP/Getting-Started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>XCP</a>, the protocol for real-time measurement and calibration of ECU parameters during development.
      </>
    ),
  },
];

function Feature({ title, description }) {
  return (
    <div className="feature-box">
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className="features">
      <div className="container">
        <div className="features-grid">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
