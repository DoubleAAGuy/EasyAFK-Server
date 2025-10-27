const mineflayer = require('mineflayer');

// Read arguments: node bot.js <username/email> <server_ip> <server_port>
const [,, username, host, port] = process.argv;

if (!username || !host || !port) {
  console.log('Usage: node bot.js <username/email> <server_ip> <server_port>');
  process.exit(1);
}

const bot = mineflayer.createBot({
  host: host,
  port: parseInt(port),
  username: username,
  auth: 'microsoft' // Use 'mojang' for legacy accounts
});

bot.on('spawn', () => {
  console.log('Bot has joined the server!');


  setTimeout(() => {
    console.log('10 hours reached. Logging out...');
    bot.quit('Time limit reached');
  }, 1 * 1 * 60 * 1000);
});
bot.on('chat', (username, message) => {
  if (username !== bot.username) bot.chat(`You said: ${message}`);
});

bot.on('kicked', (reason) => console.log(`Kicked: ${reason}`));
bot.on('error', (err) => console.log(`Error: ${err}`));
bot.on('end', () => console.log('Disconnected'));
