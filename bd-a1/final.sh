mkdir -p service-result

echo "id: "
read id

docker cp $id:/home/doc-bd-a1/res_dpre.csv ./service-result/
docker cp $id:/home/doc-bd-a1/eda-in-1.txt ./service-result/
docker cp $id:/home/doc-bd-a1/eda-in-2.txt ./service-result/
docker cp $id:/home/doc-bd-a1/eda-in-3.txt ./service-result/
docker cp $id:/home/doc-bd-a1/vis.png ./service-result/
docker cp $id:/home/doc-bd-a1/k.txt ./service-result/
docker stop $id