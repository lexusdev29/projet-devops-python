Write-Host "===== Déploiement local Projet Python DevOps ====="

$image = "lexusdev29/projet-python-devops:latest"
$container = "projet-python-devops"

Write-Host "Arrêt du conteneur..."
docker stop $container 2>$null

Write-Host "Suppression du conteneur..."
docker rm $container 2>$null

Write-Host "Récupération de l'image..."
docker pull $image

Write-Host "Lancement..."
docker run -d --name $container -p 5000:5000 $image

Write-Host "Déploiement terminé."
Write-Host "Accède : http://localhost:5000"
