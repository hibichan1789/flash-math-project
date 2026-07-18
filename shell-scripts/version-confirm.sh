#!/bin/bash
set -e

echo "====== Tool Versions ======"

echo -n "Node.js: "
node -v

echo -n "npm: "
npm -v

echo -n "Python: "
python --version

echo -n "Azure CLI: "
az --version | head -n 1

echo -n "Azure Functions Core Tools: "
func --version

echo -n "Azurite: "
azurite --version

echo "==========================="