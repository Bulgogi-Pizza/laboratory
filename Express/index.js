const express = require('express');
const app = express();
const port = 8001;

function fibonacci(n) {
  if (n <= 1) {
    return n;
  }
  return fibonacci(n - 1) + fibonacci(n - 2);
}

app.get('/', (req, res) => {
  res.json({ message: 'Hello, World!' });
});

app.get('/calculate/:number', (req, res) => {
  const number = parseInt(req.params.number, 10);
  const result = fibonacci(number);
  res.json({ number: number, fibonacci: result });
});

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});
