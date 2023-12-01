const hashFunc = (input) => {
  return '*' + input + '*';
}

class Block {
  constructor(data, hash, lastHash){
    this.data = data;
    this.hash = hash;
    this.lastHash = lastHash;
  }
}

class Blockchain {
  constructor(){
    const genesis = new Block ('gen-data', 'gen-hash', 'gen-lastHash');
    this.chain = [genesis];
  }

  addBlock(data){
    const lastHash = this.chain[this.chain.length-1].hash;
    const hash = hashFunc(data , lastHash);
    const block = new Block(data, hash, lastHash);
    this.chain.push(block);
  }
}



// const fooBlock = new Block('foo-data', 'foo-hash', 'foo-lastHash');
// console.log(fooBlock);

const fooBlockChain = new Blockchain();

fooBlockChain.addBlock('one');
fooBlockChain.addBlock('two');
fooBlockChain.addBlock('three');

console.log(fooBlockChain);