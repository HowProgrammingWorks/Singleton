'use strict';

const Singleton = (() => {
  let instance;

  function Singleton() {
    if (instance) return instance;
    instance = this;
  }

  Singleton.prototype.test = function() {};

  return Singleton;
})();

// Usage

console.assert(new Singleton() === new Singleton());
console.log('instances are equal');
