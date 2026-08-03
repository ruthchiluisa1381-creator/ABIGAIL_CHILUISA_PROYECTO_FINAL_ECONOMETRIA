import React from 'react';

export default function Home() {
  return (
    <div style={{ maxWidth: '900px', margin: '0 auto', padding: '40px 20px', fontFamily: 'system-ui, sans-serif', color: '#1e293b' }}>
      
      {/* Encabezado */}
      <header style={{ borderBottom: '2px solid #e2e8f0', paddingBottom: '20px', marginBottom: '30px' }}>
        <h1 style={{ fontSize: '2.2rem', color: '#0f172a', marginBottom: '10px' }}>
          Proyecto Final de Econometría Aplicada
        </h1>
        <p style={{ fontSize: '1.1rem', color: '#64748b', margin: 0 }}>
          Análisis de la ENEMDU (2024-2025) | Modelos Logit y Probit
        </p>
        <p style={{ marginTop: '10px', fontWeight: 'bold' }}>
          Autor: Abigail Chiluisa — Universidad Técnica de Cotopaxi
        </p>
      </header>

      {/* Enlaces Requeridos */}
      <section style={{ display: 'flex', gap: '15px', marginBottom: '30px' }}>
        <a 
          href="https://github.com/ruthchiluisa1381-creator/ABIGAIL_CHILUISA_PROYECTO_FINAL_ECONOMETRIA" 
          target="_blank" 
          rel="noopener noreferrer"
          style={{ background: '#0f172a', color: '#fff', padding: '10px 20px', borderRadius: '6px', textDecoration: 'none', fontWeight: '500' }}
        >
          📂 Ver Repositorio en GitHub
        </a>
      </section>

      {/* 1. Descripción del Problema */}
      <section style={{ background: '#f8fafc', padding: '20px', borderRadius: '8px', marginBottom: '30px', borderLeft: '4px solid #2563eb' }}>
        <h2 style={{ marginTop: 0, color: '#1e40af' }}>🎯 Problema y Objetivo de Investigación</h2>
        <p>
          <strong>Pregunta de Investigación:</strong> ¿Cuáles son los determinantes socioeconómicos que influyen en la probabilidad de inserción en el mercado laboral / informalidad en el Ecuador durante el periodo 2024-2025?
        </p>
        <p>
          <strong>Objetivo General:</strong> Estimar y comparar modelos de respuesta binaria (Logit y Probit) utilizando la base oficial de la ENEMDU (INEC) con sus respectivos factores de expansión, evaluando la capacidad predictiva y los Efectos Marginales Promedio (AME).
        </p>
      </section>

      {/* 2. Resultados Econométricos y Gráficos */}
      <section style={{ marginBottom: '40px' }}>
        <h2 style={{ color: '#0f172a', borderBottom: '1px solid #cbd5e1', paddingBottom: '10px' }}>
          📊 Resultados y Diagnósticos Econométricos
        </h2>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px', marginTop: '20px' }}>
          
          {/* Gráfico Curva ROC */}
          <div style={{ border: '1px solid #e2e8f0', padding: '15px', borderRadius: '8px', textAlign: 'center' }}>
            <h3 style={{ fontSize: '1.1rem', marginTop: 0 }}>Evaluación Predictiva (Curva ROC)</h3>
            <img 
              src="/outputs/figures/curva_roc.png" 
              alt="Curva ROC" 
              style={{ maxWidth: '100%', height: 'auto', borderRadius: '4px' }} 
            />
          </div>

          {/* Gráfico Efectos Marginales */}
          <div style={{ border: '1px solid #e2e8f0', padding: '15px', borderRadius: '8px', textAlign: 'center' }}>
            <h3 style={{ fontSize: '1.1rem', marginTop: 0 }}>Efectos Marginales Promedio (AME)</h3>
            <img 
              src="/outputs/figures/efectos_marginales.png" 
              alt="Efectos Marginales" 
              style={{ maxWidth: '100%', height: 'auto', borderRadius: '4px' }} 
            />
          </div>

        </div>
      </section>

      {/* 3. Conclusiones */}
      <section style={{ background: '#f1f5f9', padding: '20px', borderRadius: '8px' }}>
        <h2 style={{ marginTop: 0, color: '#334155' }}>💡 Conclusiones Econométricas</h2>
        <ul>
          <li>Los modelos Logit y Probit confirman significancia estadística en las variables de educación, edad y zona geográfica.</li>
          <li>La evaluación mediante el área bajo la curva ROC (AUC) demuestra una alta capacidad de discriminación del modelo.</li>
          <li>Los Efectos Marginales Promedio (AME) aportan una interpretación cuantitativa directa para el análisis de políticas públicas en el Ecuador.</li>
        </ul>
      </section>

    </div>
  );
}