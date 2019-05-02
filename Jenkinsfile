#!groovy
import groovy.json.JsonSlurperClassic
def DOCKER_BUILD_SERVER = "tcp://0.0.0.0:8000"
def DOCKER_IMAGE_REGISTRY = "gcr.io/rock-dragon-239409/"
def REPOSITORY_NAME = "gcr.io/rock-dragon-239409/5289fa94d757"


def IMAGE_NAME = "django-octapp"
def CONTAINER = "django-octapp"
def djangoImages


//def pipeline

# Version & Release Specified Here
def getVersion(def projectJson){
    def slurper = new JsonSlurperClassic()
    project = slurper.parseText(projectJson)
    slurper = null
    return project.version.split('-')[0]
}

# Repository Clone here
def CloneFromGit( REPOSITORY_NAME ){
    def version, revision
    try {
        git(branch: "${params.BRANCH}",
                changelog: true,
                credentialsId: 'FreeIPA_USERID',
                poll: true,
                url: "${REPOSITORY_NAME}"
        )
    }
    catch (Exception e) {
        println 'Some Exception happened here '
        throw e

    }
    finally {
        revision = version + "-" + sprintf("%04d", env.BUILD_NUMBER.toInteger())
        println "Start building  revision $revision"

    }
    return this
}

# Docker Image build &  Push to registry
def DockerImageBuild( DOCKER_BUILD_SERVER, DOCKER_IMAGE_REGISTRY, IMAGE_NAME ){


    // Docker Image Build & Deploy
    withDockerServer([uri: "${DOCKER_BUILD_SERVER}"]) {
        stage('IMAGE BUILD'){

            djangoImages = docker.build("${DOCKER_IMAGE_REGISTRY}/${IMAGE_NAME}")


        }

        //PUSH to Registry
        stage('PUSH IMAGE'){
            withDockerRegistry(url: "${DOCKER_IMAGE_REGISTRY}") {
                djangoImages.push("${IMAGE_NAME}:${env.BUILD_NUMBER}")
                djangoImages.push("${IMAGE_NAME}:latest")
            }


        }


    }
    return this
}

// BUILD NODE
node {


     stage('GIT CLONE') {
            CloneFromGit(REPOSITORY_NAME)

      }

     DockerImageBuild(SERVER_TO_DEPLOY,DOCKER_IMAGE_REGISTRY, IMAGE_NAME)


//NODE END
}