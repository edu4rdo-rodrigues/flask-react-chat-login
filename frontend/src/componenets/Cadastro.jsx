// frontend/src/components/Cadastro.jsx

import React from 'react';
import { useState } from "react";

function Cadastro() {
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [erro, setErro] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      nome,
      email,
      senha,
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/cadastrar/dados', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (response.status === 200) {
        // O cadastro foi bem-sucedido, limpe os campos.
        setNome('');
        setEmail('');
        setSenha('');
        setErro(null);
        console.log('Cadastro bem-sucedido!');
      } else {
        // Lidar com erros de validação ou outros problemas.
        const responseData = await response.json();
        setErro(responseData.message || 'Erro desconhecido ao cadastrar.');
      }
    } catch (error) {
      console.error('Erro na solicitação:', error);
      setErro('Erro na solicitação. Verifique sua conexão com a internet.');
    }
  };

  return (
    <div>
      <h2>Cadastro</h2>
      {erro && <p className="erro">{erro}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="nome">Nome:</label>
          <input
            type="text"
            id="nome"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="email">E-mail:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="senha">Senha:</label>
          <input
            type="password"
            id="senha"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
            required
          />
        </div>
        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
}

export default Cadastro;
