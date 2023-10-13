// frontend/src/components/Login.jsx
import React, { useState } from 'react';
import axios from 'axios';

//import { ExportVenvObject, ExportVenvArrayOfObjects } from '../exportVenv/exportVenv';
import {api_backend_url} from '../exportVenv/ExportVenv';

function Login({ setIsLogged, setUser }) {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');


  const handleSubmit = async (e) => {
    e.preventDefault();
  
    const data = {
      email,
      senha,
    };
  
    try {
      const response = await axios.post(`http://127.0.0.1:8000/login`, data);
  
      if (response.status === 200) {
        const result = response.data;

        //localStorage.setItem('sessionToken', result)
  
        // O login foi bem-sucedido, você pode lidar com a resposta aqui.
        const successLogin = ['Login bem-sucedido!', result];
        console.log('Login bem-sucedido!', result);
        console.log('Success Login!', successLogin);
  
        // Defina o estado como logado e configure as informações do usuário
        setIsLogged(true);
        setUser(result.user_info); // Define as informações do usuário no estado
      } else {
        // Lidar com erros de autenticação ou outros problemas.
        console.error('Erro ao fazer login.');
      }
    } catch (error) {
      const erroLogin = ['Erro na solicitação de Login:', error];
      console.error('Erro na solicitação:', error);
      console.error(erroLogin);
    }

  };
  
  

  return (
    <div>
      <h3>Url do API Backend do servidor Flask </h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="email">E-mail:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="senha">Senha:</label>
          <input
            type="password"
            id="senha"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;

