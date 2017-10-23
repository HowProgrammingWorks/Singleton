'use strict';

const Singleton = new (function() {
  const single = this;
  return function() { return single; };
})();

console.assert(new Singleton() === new Singleton());
