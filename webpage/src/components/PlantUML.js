// src/components/PlantUML.js
import React from 'react';
import plantumlEncoder from 'plantuml-encoder';

const PlantUML = ({ code, format = 'svg', serverUrl = 'https://www.plantuml.com/plantuml' }) => {
  // Encode the PlantUML code
  const encoded = plantumlEncoder.encode(code);
  const imageUrl = `${serverUrl}/${format}/${encoded}`;

  return (
    <div className="plantuml-diagram">
      <img src={imageUrl} alt="PlantUML diagram" />
    </div>
  );
};

export default PlantUML;
