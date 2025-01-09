import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Automotive Open System Architecture',
    description: (
      <>
        Explore <a href="/Vehicle-Network-Standards/docs/AUTOSAR/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>AUTOSAR</a>, the standardized automotive software architecture designed to improve interoperability, scalability, and software reuse across the automotive industry.
      </>
    ),
  },
  {
    title: 'Controller Area Network',
    description: (
      <>
        Learn about the widely-used <a href="/Vehicle-Network-Standards/docs/CAN/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>CAN</a> protocol, including its architecture and practical use cases in modern automotive systems. 
        .
      </>
    ),
  },
  
  
  {
    title: 'Diagnostics over IP',
    description: (
      <>
        Learn about the <a href="/Vehicle-Network-Standards/docs/DoIP/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>DoIP</a>, essential for vehicle diagnostics in modern Ethernet-based systems.
      </>
    ),
  },
  {
    title: 'Ethernet',
    description: (
      <>
        Discover the importance of <a href="/Vehicle-Network-Standards/docs/Ethernet/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>Ethernet</a> in automotive networks, supporting high-bandwidth communication for ADAS and infotainment.
      </>
    ),
  },
  {
    title: 'FlexRay',
    description: (
      <>
        Delve into the high-speed, deterministic communication offered by <a href="/Vehicle-Network-Standards/docs/FLEXRAY/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>FlexRay</a>, designed for safety-critical automotive applications.
      </>
    ),
  },
  {
    title: 'Local Interconnect Networ)',
    description: (
      <>
        Explore the simplicity and efficiency of the <a href="/Vehicle-Network-Standards/docs/LIN/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>LIN</a> protocol, ideal for low-cost, low-speed vehicle networks.
      </>
    ),
  },
  {
    title: 'Secure Onboard Communication',
    description: (
      <>
        Understand <a href="/Vehicle-Network-Standards/docs/SecOC/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>SecOC</a>, the automotive cybersecurity standard ensuring secure and reliable communication within vehicle networks.
      </>
    ),
  },
  {
    title: 'Scalable service-Oriented Middleware over IP',
    description: (
      <>
        Learn how <a href="/Vehicle-Network-Standards/docs/SOME-IP/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>SOME/IP</a> enables efficient communication in service-oriented architectures within automotive Ethernet networks.
      </>
    ),
  },
  {
    title: 'Service-Oriented Vehicle Architecture',
    description: (
      <>
        Explore <a href="/Vehicle-Network-Standards/docs/SOVA/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>SOVA</a>, the architecture that facilitates modular development and integration of vehicle services and applications.
      </>
    ),
  },
  {
    title: 'Service-Oriented Vehicle Diagnostics',
    description: (
      <>
        Gain insights into <a href="/Vehicle-Network-Standards/docs/SOVD/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>SOVD</a>, a modern approach to vehicle diagnostics leveraging service-oriented architectures for scalability and efficiency.
      </>
    ),
  },
  {
    title: 'Unified Diagnostic Services',
    description: (
      <>
        Understand <a href="/Vehicle-Network-Standards/docs/UDS/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>UDS</a>, the ISO-standardized diagnostic communication protocol used for vehicle diagnostics and ECU reprogramming in automotive systems.
      </>
    ),
  },
  {
    title: 'Universal Measurement and Calibration Protocol',
    description: (
      <>
        Learn about <a href="/Vehicle-Network-Standards/docs/XCP/getting_started" target="_self" style={{ textDecoration: 'underline', color: '#007acc' }}>XCP</a>, the protocol for real-time measurement and calibration of ECU parameters during development.
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
