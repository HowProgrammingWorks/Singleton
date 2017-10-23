'use strict';

const Singleton = (function() {
  let instance;

  function Singleton() {
    if (instance) return instance;
    instance = this;
  }

  Singleton.prototype.test = function() {};

  return Singleton;
})();

console.assert(new Singleton() === new Singleton());
