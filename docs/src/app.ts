import express from 'express';
import { setup, serveFiles } from 'swagger-ui-express';
import YAML from 'yamljs';
import fs from 'fs';
import path from 'path';

const app = express();
app.set('trust proxy', true);
app.get('/docs/ping', (_, res) => res.send({ ping: 'pong' }));

const yamlFile = YAML.load(path.resolve(__dirname, 'swagger.yaml'));
app.use(`/docs`, serveFiles(yamlFile), setup(yamlFile));

app.listen(3000, () => console.log('API Docs listening on port 3000'));
