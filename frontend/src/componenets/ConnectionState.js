// frontend/src/components/ConnectionState.js

import React from 'react';

export function ConnectionState({ isConnected }) {
  return <p>State do servidor socket: { '' + isConnected }</p>;
}