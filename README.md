# botnet infrastructure scalable to up to 300 simulated bot clients where each bot is simulated using a docker container 

## contents : 
- 'server.py' local http test server with rate limiting 
- 'bot.py' bot client
- 'Docker.file' docker image definition for a bot
- 'docker-compose.yml' orchestration and scaling

### start the server : 
'bash' 
python3 server.py
server runs locally on http://127.0.0.1:5001

#### build the bot image : 
docker compose build

##### launch bots : 
docker compose up --scale bot=300

###### stop bots:
docker compose down 
