// frontend/src/App.jsx

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { socket } from './socket.js';
import Cadastro from './componenets/Cadastro';
import Login from './componenets/Login';
import { ConnectionState } from './componenets/ConnectionState';
import { Events } from './componenets/Events';
import { ConnectionManager } from './componenets/ConnectionManager';
import { MyForm } from './componenets/MyForm';

function App() {
  const [isLogged, setIsLogged] = useState(false);
  const [user, setUser] = useState(null);
  const [isConnected, setIsConnected] = useState(socket.connected);
  const [fooEvents, setFooEvents] = useState([]);



  useEffect(() => {
    function onConnect() {
      setIsConnected(true);
      console.log('Conectado ao servidor Socket.io web');
    }

    function onDisconnect() {
      setIsConnected(false);
      console.log('Desconectado ao servidor Socket.io web');
    }

    function onFooEvent(value) {
      setFooEvents(previous => [...previous, value]);
    }

    socket.on('connect', onConnect);
    socket.on('disconnect', onDisconnect);
    socket.on('foo', onFooEvent);

    return () => {
      socket.off('connect', onConnect);
      socket.off('disconnect', onDisconnect);
      socket.off('foo', onFooEvent);
    };
  }, []);

  return (
    <div className="App">

      <Login setIsLogged={setIsLogged} setUser={setUser} user={user} />
      <Cadastro />
      
      {
        isLogged 
        ? 
          <>
            <h1>Voce esta logado</h1>
          </>
        :  
        null
      }
      
      <Events events={ fooEvents } />,
      <ConnectionState isConnected={ isConnected } />
      <ConnectionManager />,

      {
        isConnected 
        ? 
          <>
            <h3>Conetadoa ao servidor Sockect</h3> 
            <MyForm isConnected={isConnected} />
          </>
          
        : 
          <h3>Desconectado ao servidor Sockect</h3>
      }
      {/*
        isConnected ?
          <MyForm isConnected={isConnected} />
          :
          null
      */}
      
      
      
    </div>
  );
}

export default App;
