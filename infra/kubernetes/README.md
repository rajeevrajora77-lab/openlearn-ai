# Kubernetes Configuration

Kubernetes manifests for deploying OpenLearn AI to production.

## Structure

```
base/
├── namespaces/          # Namespace definitions
├── deployments/         # Service deployments
├── services/            # Service definitions
├── configmaps/          # Configuration
└── secrets/             # Secrets (not in git)

overlays/
├── development/         # Dev environment
├── staging/             # Staging environment
└── production/          # Production environment
```

## Deployment

```bash
# Apply base configuration
kubectl apply -k base/

# Apply environment-specific configuration
kubectl apply -k overlays/production/

# Check deployment status
kubectl get pods -n production
```

## Coming Soon

Complete Kubernetes manifests with:
- Helm charts
- Istio service mesh configuration
- Horizontal Pod Autoscalers
- Pod Disruption Budgets
- Network policies
