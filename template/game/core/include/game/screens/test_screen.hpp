#ifndef GAME_SCREENS_TESTSCREEN
#define GAME_SCREENS_TESTSCREEN

#include "hx3d/core/screen_adapter.hpp"

#include "hx3d/graphics/shader.hpp"
#include "hx3d/graphics/batch.hpp"

#include "hx3d/graphics/cameras/perspective_camera.hpp"

#include "hx3d/graphics/meshes/star.hpp"
#include "hx3d/graphics/meshes/origin.hpp"

class TestScreen: public hx3d::ScreenAdapter {

public:
  TestScreen();

  virtual void update() override;
  virtual void render() override;
  virtual void resize(int width, int height) override;

private:
  Ptr<hx3d::Shader> shader;
  Ptr<hx3d::PerspectiveCamera> camera;

  hx3d::Batch batch;

  hx3d::mesh::Star star;
  hx3d::mesh::Origin origin;

  float angle;
};

#endif
