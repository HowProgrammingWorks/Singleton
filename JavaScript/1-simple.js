'use strict';

function Singleton() {
  const instance = Singleton.instance;
  if (instance) return instance;
  Singleton.instance = this;
}

console.assert(new Singleton() === new Singleton());
