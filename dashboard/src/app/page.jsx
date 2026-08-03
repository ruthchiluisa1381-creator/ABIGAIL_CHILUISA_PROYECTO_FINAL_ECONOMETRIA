import React from 'react';

export default function Dashboard() {
  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: '40px', maxWidth: '1000px', margin: '0 auto', color: '#333', backgroundColor: '#f9f9f9' }}>
      
      {/* 1. Portada & Identificación */}
      <header style={{ borderBottom: '2px solid #2563eb', paddingBottom: '20px', marginBottom: '30px' }}>
        <h1 style={{ color: '#1e3a8a', marginBottom: '10px' }}>Proyecto Econométrico: Análisis ENEMDU</h1>
        <p><strong>Autor:</strong> Abigail Chiluisa</p>
        <p><strong>Enlaces de Interés:</strong> <a href="#" style={{ color: '#2563eb' }}>Repositorio de GitHub</a> | <a href="#" style={{ color: '#2563eb' }}>Documento PDF</a></p>
      </header>

      {/* 2. Problema & Pregunta de Investigación */}
      <section style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '8px', marginBottom: '20px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
        <h2 style={{ color: '#1d4ed8' }}>1. Problema & Pregunta de Investigación</h2>
        <p><strong>Pregunta:</strong> ¿Cuáles son los determinantes socioeconómicos de la informalidad laboral en Ecuador durante el periodo 2024-2025?</p>
        <p><strong>Justificación y Literatura Base:</strong> Basado en los estudios clásicos y recientes de la dinámica laboral en América Latina (p. ej., Maloney, 2004; Perry et al., 2007; Fields, 2011; ILO, 2020; Gasparini & Tornarolli, 2009).</p>
      </section>

      {/* 3. Datos y Exploratorio */}
      <section style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '8px', marginBottom: '20px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
        <h2 style={{ color: '#1d4ed8' }}>2. Datos y Exploratorio</h2>
        <p>Análisis descriptivo de las variables clave obtenidas de la encuesta ENEMDU (2024-2025).</p>
        <img src="/outputs/figures/distribución_edad_informalidad.png" alt="Distribución Edad" style={{ maxWidth: '100%', borderRadius: '6px' }} />
      </section>

      {/* 4. Resultados Econométricos */}
      <section style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '8px', marginBottom: '20px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
        <h2 style={{ color: '#1d4ed8' }}>3. Resultados Econométricos</h2>
        <p>Estimaciones de los modelos probabilísticos discrete choice (Logit y Probit) y sus Efectos Marginales Promedio (AME):</p>
        <img src="/outputs/figures/efectos_marginales.png" alt="Efectos Marginales" style={{ maxWidth: '100%', borderRadius: '6px' }} />
      </section>

      {/* 5. Diagnóstico & Matriz de Confusión */}
      <section style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '8px', marginBottom: '20px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
        <h2 style={{ color: '#1d4ed8' }}>4. Diagnóstico & Matriz de Confusión</h2>
        <p>Evaluación del poder predictivo de los modelos mediante la curva ROC y métricas AUC:</p>
        <img src="/outputs/figures/curva_roc.png" alt="Curva ROC" style={{ maxWidth: '100%', borderRadius: '6px', width: '500px' }} />
      </section>

      {/* 6. Conclusiones y Políticas Públicas */}
      <section style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '8px', marginBottom: '20px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
        <h2 style={{ color: '#1d4ed8' }}>5. Conclusiones y Recomendaciones</h2>
        <ul>
          <li>La educación y el nivel de ingresos son determinantes significativos para reducir la probabilidad de informalidad.</li>
          <li>Se recomienda focalizar programas de capacitación laboral e incentivos fiscales para la formalización de MIPYMES.</li>
        </ul>
      </section>

    </div>
  );
}
