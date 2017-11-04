## Auto-Generating a NiFi REST API Client


The NiFi project uses a Swagger spec as part of its REST API backend. This can be coupled with the swagger-codegen project to automatically generate a REST API client in over 20 different languages.


### Grab and build NiFi locally

```zsh
brew install maven && \
mkdir -p $HOME/apisland && cd $HOME/apisland && \
git clone git@github.com:apache/nifi.git && \
cd nifi/ && \
git co tags/rel/1.4.0 && \
mvn clean package -Dmaven.test.skip=true && \
find . | grep swagger.json$
```

After a long maven build process, you should see something like...

```zsh
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 11:42 min
[INFO] Finished at: 2017-11-04T16:45:19-04:00
[INFO] Final Memory: 327M/1828M
[INFO] ------------------------------------------------------------------------
nifi nifi-1.4.0-apisland % ls
KEYS                  nifi-api              nifi-docs             nifi-nar-bundles
LICENSE               nifi-assembly         nifi-external         nifi-toolkit
NOTICE                nifi-bootstrap        nifi-framework-api    pom.xml
README.md             nifi-commons          nifi-maven-archetypes target
appveyor.yml          nifi-docker           nifi-mock
nifi nifi-1.4.0-apisland % find . | grep swagger.json$
./nifi-nar-bundles/nifi-framework-bundle/nifi-framework/nifi-web/nifi-web-api/target/swagger-ui/swagger.json
```
Wohoo! We have our target Swagger spec and can go about the codegen.


### Grab and build Swagger-codegen locally

```zsh
cd $HOME/apisland && \
git clone https://github.com/swagger-api/swagger-codegen && \
cd swagger-codegen && \
mvn clean package
```

Now let's generate our api-client for `python`. Swagger codegen should aim for a client that's compatible with both python2 and python3, so no worries there.


### Generate and inspect the Python client

```zsh
mkdir -p $HOME/apisland/nifi-api-clients/python/nifi-1.4.0/ && \
cd $HOME/apisland/swagger-codegen && \
java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
-i $HOME/apisland/nifi/nifi-nar-bundles/nifi-framework-bundle/nifi-framework/nifi-web/nifi-web-api/target/swagger-ui/swagger.json \
-l python \
-o $HOME/apisland/nifi-api-clients/python/nifi-1.4.0
```

```
swagger-codegen master % cd ~/dev/cms/pynifi-1.4.0

pynifi-1.4.0 % ls
README.md             requirements.txt      test
docs                  setup.py              test-requirements.txt
git_push.sh           swagger_client        tox.ini

pynifi-1.4.0 % vim #poke around the generated files

pynifi-1.4.0 % ls
README.md             requirements.txt      test                  venv
docs                  setup.py              test-requirements.txt
git_push.sh           swagger_client        tox.ini

pynifi-1.4.0 % python3 -m venv venv
pynifi-1.4.0 % source venv/bin/activate

(venv) pynifi-1.4.0 % pip install -e .
Obtaining file:///Users/ajish/dev/cms/pynifi-1.4.0
Collecting urllib3>=1.15 (from swagger-client==1.0.0)
  Using cached urllib3-1.22-py2.py3-none-any.whl
Collecting six>=1.10 (from swagger-client==1.0.0)
  Using cached six-1.11.0-py2.py3-none-any.whl
Collecting certifi (from swagger-client==1.0.0)
  Using cached certifi-2017.7.27.1-py2.py3-none-any.whl
Collecting python-dateutil (from swagger-client==1.0.0)
  Using cached python_dateutil-2.6.1-py2.py3-none-any.whl
Installing collected packages: urllib3, six, certifi, python-dateutil, swagger-client
  Running setup.py develop for swagger-client
Successfully installed certifi-2017.7.27.1 python-dateutil-2.6.1 six-1.11.0 swagger-client urllib3-1.22

(venv) pynifi-1.4.0 % python setup.py test
Test VariableRegistryUpdateRequestEntity ... ok
testVariableRegistryUpdateStepDTO (test.test_variable_registry_update_step_dto.TestVariableRegistryUpdateStepDTO)
Test VariableRegistryUpdateStepDTO ... ok
testVersionInfoDTO (test.test_version_info_dto.TestVersionInfoDTO)
Test VersionInfoDTO ... ok

----------------------------------------------------------------------
Ran 794 tests in 37.939s

OK
(venv) pynifi-1.4.0 % 
```

#### TODO: Stand up some integration tests w/ local NiFi

