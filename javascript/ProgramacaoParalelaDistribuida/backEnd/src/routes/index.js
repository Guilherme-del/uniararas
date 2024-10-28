/**
 * Arquivo: src/routes/index.js
 * Descrição: arquivo responsável pela chamada da Api 'Funcionário' da aplicação.
 * Data: 09/06/2024
 * Author: Guilherme Cavenaghi
 */

const express = require('express');

const router = express.Router();

router.get('/', (req, res) => {
  res.status(200).send({
    success: 'true',
    message: 'Seja bem-vindo(a) a API Mean',
    version: '1.0.0',
  });
});

module.exports = router;
