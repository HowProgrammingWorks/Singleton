'use strict';

const init = require('eslint-config-metarhia');

module.exports = [
  ...init,
  {
    rules: {
      'class-methods-use-this': 'off',
      'no-self-compare': 'off',
      'no-extra-parens': 'off',
      'no-invalid-this': 'off',
   },
  },
];
