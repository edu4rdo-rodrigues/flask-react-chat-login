// frontend/src/components/Login.jsx
import React, { useState } from 'react';
import axios from 'axios';

//import { ExportVenvObject, ExportVenvArrayOfObjects } from '../exportVenv/exportVenv';
import { API_BACKEND_URL } from '../varEnv/exportVenv';
console.log(API_BACKEND_URL);
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
      const response = await axios.post(`${API_BACKEND_URL}/login`, data);
  
      if (response.status === 200) {
        const result = response.data;

        //localStorage.setItem('sessionToken', result)
  
        // O login foi bem-sucedido, você pode lidar com a resposta aqui.
        const successLogin = ['Login bem-sucedido!', result];
        console.log('Frontend: Login bem-sucedido!', result);
        console.log('Frontend: Success Login!', successLogin);
  
        // Defina o estado como logado e configure as informações do usuário
        setIsLogged(true);
        setUser(result.user_info); // Define as informações do usuário no estado
      } else {
        // Lidar com erros de autenticação ou outros problemas.
        console.error('Frontend: Erro ao fazer login.');
      }
    } catch (error) {
      const erroLogin = ['Frontend: Erro na solicitação de Login:', error];
      console.error('Frontend: Erro na solicitação:', error);
      console.error(erroLogin);
    }

  };
  
  

  return (
    <div>
      <h3>Url do API Backend do servidor Flask </h3>
      <form onSubmit={handleSubmit}>
        <button type="submit">Logout</button>
      </form>
    </div>
  );
}

export default Login;

