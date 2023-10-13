// src/utils/socket.js
import React from 'react';
import { io } from 'socket.io-client';
import { api_socket_url } from './exportVenv/ExportVenv';

export const socket = io(`http://localhost:3000`);
    


