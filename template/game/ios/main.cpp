#include "hx3d/window/sdl2/sdl2_application.hpp"
#include "hx3d/window/application_config.hpp"

#include "game/<#[game_name_lower]#>.hpp"

using namespace hx3d;

int main(int argc, char** argv) {
  ApplicationConfig config;
  SDL2Application app(Make<<#[game_name]#>>(), config);
  app.start();

  return 0;
}
