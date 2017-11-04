
# TODOs

1. Add integration tests using NiFi-local/NiFi-docker
2. Refactor so that multiple versions of the NiFi DTOs and Entities can be supported by one client library.
3. MVP/Least effort for the above would be to use releases/branches with installs managed by pip.
4. Investigate whether the DTOs/Entities and REST API are backwards compatible for the primary versions of NiFi
6. Proper cookiecutter based package layout
7. Jenkins
8. Hookup the usual badges, for build quality.
9. Compare to directly wrapping NiFi DTOs in a JVM lang -- Scala/Akka, Clojure, or if we must jython/kotlin/groovy.
10. Also integrate http-prompt against same swagger. See [![asciicast](https://asciinema.org/a/96613.png)](https://asciinema.org/a/96613?theme=monokai&size=medium&autoplay=1&speed=1.5)
