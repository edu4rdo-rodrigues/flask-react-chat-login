// src/utils/socket.js
import React from 'react';
import { io } from 'socket.io-client';

export const socket = io(`http://localhost:5000`);
    


