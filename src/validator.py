const logger = require('winston');

logger.configure({
    level: 'info',
    format: logger.format.simple(),
    transports: [new logger.transports.Console()]
});

async function main() {
    logger.info('Starting application...');
    try {
        // TODO: Add your code here
        logger.info('Application running successfully');
    } catch (error) {
        logger.error(`Error: ${error.message}`);
        process.exit(1);
    }
}

main().catch(console.error);
