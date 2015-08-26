#include "hx3d/core/application.hpp"
#include "game/osef.hpp"

using namespace hx3d;

int main(int argc, char** argv) {

  ApplicationConfig config;
  Application app(Make<<#[game_name]#>>(), config);

  return 0;
}
