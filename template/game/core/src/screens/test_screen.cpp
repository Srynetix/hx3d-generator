#include "game/screens/test_screen.hpp"

#include "hx3d/core/core.hpp"
#include "hx3d/core/application.hpp"
#include "hx3d/core/game.hpp"
#include "hx3d/core/events.hpp"

#include "hx3d/graphics/framebuffer.hpp"

#include "hx3d/math/random.hpp"

#include "hx3d/utils/log.hpp"
#include "hx3d/utils/assets.hpp"

using namespace hx3d;

TestScreen::TestScreen():
  shader(Core::Assets()->get<Shader>("base")),
  camera(0.1f, 100.f)
{
  camera.translate(glm::vec3(0.f, 0.f, -5.f));
  camera.rotate(180.f, glm::vec3(0, 1, 0));

  batch.setCamera(camera);
  batch.setShader(shader);

  origin.transform.position = glm::vec3(0);
  origin.transform.size = glm::vec3(0.5f);

  angle = 0.f;
}

void TestScreen::update() {
  camera.rotateAround(glm::vec3(0.f, 0.f, 0.f), 1.f, glm::vec3(0, 1, 0));

  if (Core::CurrentSystem == Core::SystemType::Android) {
    if (Core::Events()->isKeyJustPressed(KeyEvent::Key::AndroidBack)) {
      Core::CurrentGame()->stop();
    }
  }

  if (Core::Events()->isKeyPressed(KeyEvent::Key::Escape)) {
    Core::CurrentGame()->stop();
  }

  camera.update();
}

void TestScreen::resize(int width, int height) {
}

void TestScreen::render() {

  Framebuffer::clear(Color(0, 0, 0));

  batch.begin();

  star.transform.size = glm::vec3(0.3f);
  star.transform.position.x = 0;
  star.transform.position.y = 0;
  star.transform.position.z = 0;
  star.transform.rotation.x = std::sin(glm::radians(angle * 10));
  star.transform.rotation.y = glm::radians(angle * 2);
  batch.draw(star);

  star.transform.size = glm::vec3(0.1f);
  star.transform.rotation.y = glm::radians(-angle * 4);

  star.transform.position.x = -0.75f;
  batch.draw(star);

  star.transform.position.x = 0.f;
  star.transform.position.z = -0.75f;
  batch.draw(star);

  star.transform.position.x = 0.75f;
  star.transform.position.z = 0.f;
  batch.draw(star);

  star.transform.position.x = 0;
  star.transform.position.z = 0.75f;
  batch.draw(star);

  star.transform.position.y = 0.75f;
  star.transform.position.z = 0;
  batch.draw(star);

  star.transform.position.y = -0.75f;
  batch.draw(star);

  batch.draw(origin);

  angle += 0.5f;
  if (angle > 360.f) {
    angle -= 360.f;
  }

  batch.end();
}
