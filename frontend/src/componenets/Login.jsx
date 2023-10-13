// frontend/src/components/Login.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

//import { ExportVenvObject, ExportVenvArrayOfObjects } from '../exportVenv/exportVenv';
import { API_BACKEND_URL } from '../varEnv/exportVenv';

function Login({ setIsLogged, setUser, user }) {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [nome, setNome] = useState('')
  const [newUser, setNewUser] = useState()


  
  useEffect(() => {
    if (user) {

      // Faça uma solicitação GET para buscar o nome do usuário com base no ID.
      axios.get(`${API_BACKEND_URL}/user/${user.id}`)
        .then(response => {
          if (response.status === 200) {
            const userData = response.data;
            setNome(userData.name) 
            console.log('Nome do usuário:', userData.name);
            console.log('Nome do usuário:', userData);
            const userRes = user
            userRes.nome = userData.name

           
            console.log("userRes", userRes);
            console.log("user", user);
            console.log("newUser", newUser);

            setUser(user)

          } else {
            console.error('Erro ao buscar o nome do usuário.');
          }
        })
        .catch(error => {
          console.error('Erro na solicitação:', error);
        });
    }
  },[user])


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

        console.log("Result: ", result);
        console.log("Result e User Info: ", result.user_info);

  
        // O login foi bem-sucedido, você pode lidar com a resposta aqui.
        const successLogin = ['Login bem-sucedido!', result];

        console.log('Frontend: Login bem-sucedido!', result);
        console.log('Frontend: Success Login!', successLogin);
  
        // Defina o estado como logado e configure as informações do usuário
        setIsLogged(true);
        setUser(result.user_info);
        
        //VerificaStateUser()

        // Define as informações do usuário no estado
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
      { 
        user
        ?
          <>
            <p>ID: {user.id}</p>
            <p>Nome: {user.email}</p>
            <p>Email: {user.email}</p>
            <p>Senha: {user.senha}</p>
          </>
        :
          <p>Nada</p>

      }
      <button onClick={()=> VerificaStateUser()}>Verifica o state "user"</button>
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

