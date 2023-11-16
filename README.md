echo "# Proyecto GitFlow

Este repositorio contiene el proyecto GitFlow con las configuraciones y cambios realizados siguiendo un flujo de trabajo específico.

## Pasos Realizados

### 1. Inicializar el Proyecto con GitFlow

\`\`\`bash
git clone https://github.com/tu_usuario/gitflow.git
cd gitflow
git flow init
\`\`\`

### 2. Crear al Menos 2 Ramas 'Feature'

\`\`\`bash
git checkout develop

# Para la primera característica
git flow feature start feature1
# Trabaja en tus cambios y realiza commits
git flow feature finish feature1

# Para la segunda característica
git flow feature start feature2
# Trabaja en tus cambios y realiza commits
git flow feature finish feature2
\`\`\`

### 3. Crear una Rama 'Hotfix' con un Cambio Aplicado a Main

\`\`\`bash
git checkout main
git flow hotfix start hotfix1
# Realiza los cambios necesarios y realiza commits
git flow hotfix finish hotfix1
\`\`\`

### 4. Rama Main con al Menos 3 Versiones

\`\`\`bash
git checkout main
# Crea y fusiona nuevas características para tener al menos 3 versiones
# Repite el proceso de crear características y fusionarlas con 'develop'
git tag v1.0
git tag v1.1
git tag v1.2
\`\`\`

### 5. Crear la Rama 'Develop' con al Menos 3 Cambios

\`\`\`bash
git checkout develop
# Realiza cambios y commits en 'develop'
# Repite este proceso al menos tres veces
\`\`\`

### 6. Crear una Rama de Release

\`\`\`bash
git checkout develop
git flow release start release1
# Realiza los cambios finales y ajustes necesarios para la versión de lanzamiento
git flow release finish release1
\`\`\`

### 7. Enviar a GitHub

\`\`\`bash
# Asegúrate de estar en la rama 'develop' o 'main'
git push origin develop  # O 'main' si estás utilizando 'main' en lugar de 'develop'
\`\`\`

## Herramienta Gráfica para Git

Se recomienda el uso de una herramienta gráfica para visualizar el flujo de trabajo de Git. Algunas opciones incluyen:

- [GitKraken](https://www.gitkraken.com/)
- [Sourcetree](https://www.sourcetreeapp.com/)
- [GitHub Desktop](https://desktop.github.com/)

Descarga e instala la herramienta de tu elección para una experiencia visual más fácil." > README.md
