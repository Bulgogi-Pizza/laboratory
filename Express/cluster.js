const cluster = require('cluster');
const os = require('os');

if (cluster.isMaster) {
  const cpuCount = os.cpus().length;
  console.log(`마스터 프로세스 (PID: ${process.pid}) 실행 중`);
  console.log(`${cpuCount}개의 CPU 코어를 활용하여 워커를 생성합니다.`);

  for (let i = 0; i < cpuCount; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker, code, signal) => {
    console.log(`${worker.process.pid}번 워커가 종료되었습니다. 새로운 워커를 생성합니다.`);
    cluster.fork();
  });
} else {
  // 워커 프로세스들은 기존의 index.js 파일을 실행합니다.
  require('./index.js');
}