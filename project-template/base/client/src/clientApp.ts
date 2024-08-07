/**  
 * 神岛Arena客户端入口文件clientApp.ts  
 * 1. 当你看到此文件时，表示脚手架已成功创建了项目的基础结构，你可以在这里开始编写你的 TypeScript 代码。  
 * 2. 代码中的智能提示功能已经默认配置完毕，将直接提供神岛API的提示信息，无需进行额外的配置。  
 * 3. 请注意，Arena可能不完全支持所有TypeScript代码特性或第三方库，因此在引入外部包或编写特定代码时，请务必谨慎测试，以确保兼容性和稳定性。  
 * 4. 若需查看更多关于神岛开发的指南、最佳实践或文档，请访问：https://www.yuque.com/box3lab/doc/fi2z90g00qp2hwac
 */

// daopy 需要部分
import * as TextEncodingPolyfill from 'text-encoding';
globalThis.TextEncoder = TextEncodingPolyfill.TextEncoder;
globalThis.TextDecoder = TextEncodingPolyfill.TextDecoder;
import './_daopy_bundle' // 执行daopy代码
// daopy 需要部分结束