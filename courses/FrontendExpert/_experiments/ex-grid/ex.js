function mystery() {
    let num = 0;
    return { getNum: () => num, increment: () => num++ };
  }
  const { getNum, increment } = mystery();
  const { getNum: getNum2, increment: increment2 } = mystery();
  increment();
  increment();
  increment2();
  console.log(getNum(), getNum2());