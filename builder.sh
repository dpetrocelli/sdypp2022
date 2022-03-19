random=$((1 + $RANDOM % 100))
mv  .github/workflows/cicd_pipeline* ".github/workflows/cicd_pipeline$random.yml"
git add . ; git commit -m "$random push" ; git push 