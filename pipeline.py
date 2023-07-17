import subprocess


#modificat la imageName,containerRegistryUsername 
cmd = [['./pipeline.py', 'build', '--dockerFilePath=', '.', '--imageName=myapp', '--imageTag=latest'],
       ['./pipeline.py', 'push', 'containerRegistryUsername=petru mariuta', '--imageName=myapp', '--imageTag=latest' ],
       ['./pipeline.py deploy',  '--flavour=docker','--imageName=project/myapp','--imageTag=latest'],
       ['./pipeline.py test', '--endpoint=http://localhost:5000']]

#kube = ['./pipeline.py deploy','--flavour=kubernetes', 'deploymentManifest=manifests/service.yaml',
#        '--imageName=project\/myapp', '--imageTag=latest']

for i in cmd:
    print("ok")
    #subprocess.run(i,shell=True)
cmd2 = ['pwd']
#subprocess.run(cmd2, shell=True)
#subprocess.run(kube)

