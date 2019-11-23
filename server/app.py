from flask_migrate import Migrate
import config
from db import queries

# Get the application instance
connex_app = config.connex_app
flask_app = connex_app.app
migrate = Migrate(flask_app, config.db, render_as_batch=True) 

# Configuring login functionality
config.lm.init_app(flask_app)

@config.lm.user_loader
def load_user(user_id):
    return queries.getUserByID(user_id)

# Read the swagger.yml file to configure the endpoints
connex_app.add_api('swagger.yml')

if __name__ == '__main__':
    connex_app.run(debug=True, host='192.168.1.22')