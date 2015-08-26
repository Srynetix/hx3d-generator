#include "hx3d/core/application.hpp"
#include "hx3d/core/application_config.hpp"

#include "game/<#[game_name_lower]#>.hpp"

using namespace hx3d;

int main(int argc, char** argv) {
  ApplicationConfig config;
  Application app(Make<<#[game_name]#>>(), config);

  return 0;
}
