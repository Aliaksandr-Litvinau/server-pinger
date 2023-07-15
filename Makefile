postgres: ## Run postgres for local development
	@docker run -d -p 5432:5432 \
                  -e POSTGRES_PASSWORD=postgres \
                  -e POSTGRES_USER=postgres \
                  -e POSTGRES_DB=pinger_db \
                  --name pinger_db \
                  --restart always \
                  postgres:15;

#redis:
#	@docker run --name pinger_redis \
#                -p 6379:6379 \
#                -d redis;


